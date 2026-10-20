"""Offline event canonicalization. Does not interface with a car."""
from dataclasses import dataclass
from typing import Optional
import unicodedata

TURNS = {'left':'LEFT','right':'RIGHT','slight_left':'SLIGHT_LEFT',
         'slight_right':'SLIGHT_RIGHT','straight':'STRAIGHT',
         'uturn':'UTURN','roundabout':'ROUNDABOUT','destination':'DESTINATION',
         'merge_left':'MERGE_LEFT','merge_right':'MERGE_RIGHT'}

@dataclass(frozen=True)
class Event:
    app: str
    maneuver: str
    distance_m: int
    road: str = ''
    lanes: Optional[list] = None
    active: bool = True

def simplify_street(text: str, max_len: int = 24) -> str:
    # Conservative fallback for old HUD: ASCII only. Cyrillic may not render.
    # Latin fallback for green HUD: transliterate Cyrillic rather than rendering '?'.
    translit = {
        'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo','ж':'zh',
        'з':'z','и':'i','й':'y','к':'k','л':'l','м':'m','н':'n','о':'o',
        'п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh','ц':'ts',
        'ч':'ch','ш':'sh','щ':'shch','ъ':'','ы':'y','ь':'','э':'e','ю':'yu','я':'ya',
    }
    out = []
    for ch in unicodedata.normalize('NFKD', text):
        if unicodedata.combining(ch):
            continue
        repl = translit.get(ch.lower())
        if repl is not None:
            out.append(repl.capitalize() if ch.isupper() else repl)
        elif ord(ch) < 128 and ch.isprintable():
            out.append(ch)
        else:
            out.append('?')
    return ''.join(out)[:max_len]

def normalize(payload: dict, profile: str='green_prefacelift') -> dict:
    if profile not in ('green_prefacelift','extended_hud'):
        raise ValueError('Unknown HUD profile')
    ev=Event(app=str(payload.get('app','unknown')),
             maneuver=str(payload.get('maneuver','')).lower(),
             distance_m=int(payload.get('distance_m',0)),
             road=str(payload.get('road','')),
             lanes=payload.get('lanes'),
             active=bool(payload.get('active',True)))
    if not ev.active:
        return {'active':False}
    if ev.maneuver not in TURNS:
        raise ValueError('Unsupported maneuver: '+ev.maneuver)
    if ev.distance_m < 0 or ev.distance_m > 2000000:
        raise ValueError('Invalid distance')
    out={'active':True,'icon':TURNS[ev.maneuver], 'distance_m':ev.distance_m}
    if profile=='extended_hud':
        out['road_fallback']=simplify_street(ev.road)
        out['lanes']=ev.lanes if isinstance(ev.lanes,list) else []
    return out
