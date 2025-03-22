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
            "CHEM 107": ClassInfo(rooms={}),
            "CHEM 117": ClassInfo(rooms={}),
            "ENGL 103": ClassInfo(rooms={}),
            "ENGL 104": ClassInfo(rooms={}),
            "ENGR 102": ClassInfo(rooms={"ZACH": 28, "BLOC": 40, "ILCB": 31}),
            "MATH 151": ClassInfo(rooms={}),
            "ENGR 216": ClassInfo(rooms={"ZACH": 10, "BLOC": 12, "HELD": 28}),
            "PHYS 216": ClassInfo(rooms={"MPHY": 10, "BLOC": 12, "HELD": 28}),
            "MATH 152": ClassInfo(rooms={}),
            "PHYS 206": ClassInfo(rooms={}),
            "CHEM 120": ClassInfo(rooms={}),
            "PHYS 207": ClassInfo(rooms={}),
            "MATH 251": ClassInfo(rooms={}),
            "MEEN 210": ClassInfo(rooms={}),
            "MEEN 260": ClassInfo(rooms={}),
            "MEEN 222": ClassInfo(rooms={}),
            "MEEN 225": ClassInfo(rooms={"ZACH": 40, "JCAIN": 28}),
            "MEEN 315": ClassInfo(rooms={}),
            "MATH 308": ClassInfo(rooms={}),
            "MEEN 344": ClassInfo(rooms={}),
            "MEEN 345": ClassInfo(rooms={}),
            "MEEN 360": ClassInfo(rooms={}),
            "MEEN 361": ClassInfo(rooms={}),
            "MEEN 364": ClassInfo(rooms={}),
            "ISEN 302": ClassInfo(rooms={}),
            "MEEN 363": ClassInfo(rooms={}),
            "MEEN 368": ClassInfo(rooms={}),
            "MEEN 381": ClassInfo(rooms={}),
            "MEEN 401": ClassInfo(rooms={}),
            "MEEN 461": ClassInfo(rooms={}),
            "MEEN 402": ClassInfo(rooms={}),
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
