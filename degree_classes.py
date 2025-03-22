from dataclasses import dataclass
from typing import Dict

@dataclass
class ClassInfo:
    rooms: Dict[str, int]

@dataclass
class DegreePlan:
    name: str
    classes: Dict[str, ClassInfo]

def get_degree_class_data():
    MEEN = DegreePlan(
        name="MEEN",
        classes={
            "CHEM 107": ClassInfo(rooms={"ILCB": 50}),
            "CHEM 117": ClassInfo(rooms={"HELD": 50}),
            "ENGL 103": ClassInfo(rooms={}),
            "ENGL 104": ClassInfo(rooms={}),
            "ENGR 102": ClassInfo(rooms={"ZACH": 28, "BLOC": 40, "ILCB": 31}),
            "MATH 151": ClassInfo(rooms={"ILCB": 40, "HEB": 20}),
            "ENGR 216": ClassInfo(rooms={"ZACH": 50, "BLOC": 12, "HELD": 28}),
            "PHYS 216": ClassInfo(rooms={"ZACH": 50, "BLOC": 12, "HELD": 28}),
            "MATH 152": ClassInfo(rooms={"ILCB": 50, "HEB": 20 }),
            "PHYS 206": ClassInfo(rooms={"MPHY": 50}),
            "CHEM 120": ClassInfo(rooms={}),
            "PHYS 207": ClassInfo(rooms={}),
            "MATH 251": ClassInfo(rooms={"HELD": 50}),
            "STAT 211": ClassInfo(rooms={"HECC": 50}),
            "ECEN 215": ClassInfo(rooms={"ZACH": 50}),
            "ENGR 217": ClassInfo(rooms={"ZACH": 50}),
            "PHYS 217": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 210": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 260": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 223": ClassInfo(rooms={"HECC": 50}),
            "MEEN 225": ClassInfo(rooms={"ZACH": 40, "JCAIN": 28}),
            "MEEN 315": ClassInfo(rooms={"ZACH": 50}),
            "MATH 308": ClassInfo(rooms={"BLOC": 50}),
            "MEEN 305": ClassInfo(rooms={"JCAIN": 50}),
            "MEEN 344": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 345": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 357": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 360": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 361": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 364": ClassInfo(rooms={"JCAIN": 50}),
            "MEEN 365": ClassInfo(rooms={"ZACH": 50}),
            "ISEN 302": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 363": ClassInfo(rooms={"HECC": 40, "JCAIN": 28 }),
            "MEEN 368": ClassInfo(rooms={"HECC": 40}),
            "MEEN 381": ClassInfo(rooms={"ARCB": 20}),
            "MEEN 401": ClassInfo(rooms={"JCAIN": 50}),
            "MEEN 461": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 464": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 423": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 439": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 442": ClassInfo(rooms={"ZACH": 50}),
            "MEEN 402": ClassInfo(rooms={"JCAIN": 50,"ZACH": 20}),
            "MEEN 404": ClassInfo(rooms={}),
            "MEEN 405": ClassInfo(rooms={}),
            # Additional electives that we are FORCED to take :(
        }
    )

    CHEM = DegreePlan(
        name="CHEM",
        classes={
            "CHEM 100": ClassInfo(rooms={}),
            "CHEM 119": ClassInfo(rooms={}),
            "ENGL 104": ClassInfo(rooms={}),
            "ENGL 210": ClassInfo(rooms={}),
            "MATH 151": ClassInfo(rooms={}),
            "MATH 171": ClassInfo(rooms={}),
            "CHEM 120": ClassInfo(rooms={"CHEM": 110, "HELD": 28, "HEB": 7}),
            "MATH 152": ClassInfo(rooms={}),
            "MATH 172": ClassInfo(rooms={}),
            "CHEM 227": ClassInfo(rooms={"ILCB": 210, "CHEM": 20}),
            "CHEM 237": ClassInfo(rooms={}),
            "CHEM 228": ClassInfo(rooms={"ILCB": 210, "CHEM": 20}),
            "CHEM 238": ClassInfo(rooms={}),
            "CHEM 315": ClassInfo(rooms={}),
            "CHEM 318": ClassInfo(rooms={}),
            "CHEM 327": ClassInfo(rooms={}),
            "CHEM 328": ClassInfo(rooms={}),
            "CHEM 362": ClassInfo(rooms={}),
            "CHEM 383": ClassInfo(rooms={}),
            "CHEM 412": ClassInfo(rooms={}),
            "CHEM 413": ClassInfo(rooms={}),
            "CHEM 414": ClassInfo(rooms={}),
            "CHEM 415": ClassInfo(rooms={}),
            "CHEM 446": ClassInfo(rooms={}),
            "CHEM 456": ClassInfo(rooms={}),
            "CHEM 463": ClassInfo(rooms={}),
            "CHEM 464": ClassInfo(rooms={}),
            "CHEM 466": ClassInfo(rooms={}),
            "CHEM 468": ClassInfo(rooms={}),
            "CHEM 481": ClassInfo(rooms={}),
            "CHEM 483": ClassInfo(rooms={}),
            "CHEM 485": ClassInfo(rooms={}),
            "CHEM 491": ClassInfo(rooms={}),
            # Additional electives 
        }
    )

    CSCE = DegreePlan(
        name="CSCE",
        classes={
            "CSCE 121": ClassInfo(rooms={}),
            "CSCE 181": ClassInfo(rooms={}),
            "MATH 151": ClassInfo(rooms={}),
            "MATH 171": ClassInfo(rooms={}),
            "ENGL 104": ClassInfo(rooms={}),
            "PHYS 206": ClassInfo(rooms={}),
            "PHYS 226": ClassInfo(rooms={}),
            "CSCE 221": ClassInfo(rooms={}),
            "CSCE 222": ClassInfo(rooms={}),
            "CSCE 312": ClassInfo(rooms={}),
            "CSCE 313": ClassInfo(rooms={}),
            "CSCE 314": ClassInfo(rooms={}),
            "CSCE 315": ClassInfo(rooms={}),
            "CSCE 411": ClassInfo(rooms={}),
            "CSCE 433": ClassInfo(rooms={}),
            "CSCE 481": ClassInfo(rooms={}),
            "CSCE 482": ClassInfo(rooms={}),
            "MATH 304": ClassInfo(rooms={}),
            "MATH 308": ClassInfo(rooms={}),
            "STAT 211": ClassInfo(rooms={}),
            # Additional electives 
        }
    )

    return {"MEEN": MEEN, "CHEM": CHEM, "CSCE": CSCE}
