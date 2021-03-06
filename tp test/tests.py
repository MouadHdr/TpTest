from TaskManager import TaskManager
from Task import Task


def parseEmptyInput():
    tm = TaskManager()
    tm.exec("")
    assert tm.action.type is None


def parseInputActionAdd():
    tm = TaskManager()
    tm.exec("+ Acheter du pain")
    assert tm.action.type == "ADD"


def parseInputActionRemove():
    tm = TaskManager()
    tm.exec("+ Acheter du pain")
    tm.exec("- 1")
    assert tm.action.type == "REMOVE"


def parseInputActionDone():
    tm = TaskManager()
    tm.exec("+ Acheter du pain")
    tm.exec("x 1")
    assert tm.action.type == "DONE"


def parseInputActionToDo():
    tm = TaskManager()
    tm.exec("+ Acheter du pain")
    tm.exec("o 1")
    assert tm.action.type == "TODO"


def test_parseInput():
    parseEmptyInput()
    parseInputActionAdd()
    parseInputActionRemove()
    parseInputActionDone()
    parseInputActionToDo()


def test_saveOneTask():
    tm = TaskManager()
    tm.exec("+ Acheter du pain")
    assert tm.tasks[0].label == "Acheter du pain"
    assert tm.tasks[0].status == "TODO"


def test_doneTask():
    tm = TaskManager()
    tm.exec("+ Acheter du pain")
    tm.exec("x 1")
    assert tm.tasks[0].status == "DONE"


def test_toDoTask():
    tm = TaskManager()
    tm.exec("+ Acheter du pain")
    tm.exec("x 1")
    tm.exec("o 1")
    assert tm.tasks[0].status == "TODO"
