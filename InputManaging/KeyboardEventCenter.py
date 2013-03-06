import ogre.io.OIS as OIS

class KeyboardEventCenter(object):

    # Event Action Queues----------------------------------------------------------------------------------------------#
    keyActionQueues = {
        OIS.KC_1:[],
        OIS.KC_2:[],
        OIS.KC_3:[],
        OIS.KC_4:[],
        OIS.KC_5:[],
        OIS.KC_6:[],
        OIS.KC_7:[],
        OIS.KC_8:[],
        OIS.KC_9:[],
        OIS.KC_0:[],
        OIS.KC_Q:[],
        OIS.KC_W:[],
        OIS.KC_E:[],
        OIS.KC_R:[],
        OIS.KC_T:[],
        OIS.KC_Y:[],
        OIS.KC_U:[],
        OIS.KC_I:[],
        OIS.KC_O:[],
        OIS.KC_P:[],
        OIS.KC_A:[],
        OIS.KC_S:[],
        OIS.KC_D:[],
        OIS.KC_F:[],
        OIS.KC_G:[],
        OIS.KC_H:[],
        OIS.KC_J:[],
        OIS.KC_K:[],
        OIS.KC_L:[],
        OIS.KC_Z:[],
        OIS.KC_X:[],
        OIS.KC_C:[],
        OIS.KC_V:[],
        OIS.KC_B:[],
        OIS.KC_N:[],
        OIS.KC_M:[],
        OIS.KC_RETURN:[],
        OIS.KC_ESCAPE:[]
    }
    keyDefaultAction = {
        OIS.KC_1:[],
        OIS.KC_2:[],
        OIS.KC_3:[],
        OIS.KC_4:[],
        OIS.KC_5:[],
        OIS.KC_6:[],
        OIS.KC_7:[],
        OIS.KC_8:[],
        OIS.KC_9:[],
        OIS.KC_0:[],
        OIS.KC_Q:[],
        OIS.KC_W:[],
        OIS.KC_E:[],
        OIS.KC_R:[],
        OIS.KC_T:[],
        OIS.KC_Y:[],
        OIS.KC_U:[],
        OIS.KC_I:[],
        OIS.KC_O:[],
        OIS.KC_P:[],
        OIS.KC_A:[],
        OIS.KC_S:[],
        OIS.KC_D:[],
        OIS.KC_F:[],
        OIS.KC_G:[],
        OIS.KC_H:[],
        OIS.KC_J:[],
        OIS.KC_K:[],
        OIS.KC_L:[],
        OIS.KC_Z:[],
        OIS.KC_X:[],
        OIS.KC_C:[],
        OIS.KC_V:[],
        OIS.KC_B:[],
        OIS.KC_N:[],
        OIS.KC_M:[],
        OIS.KC_RETURN:[],
        OIS.KC_ESCAPE:[]
    }
    # -----------------------------------------------------------------------------------------------------------------#

    @classmethod
    def executeKeyActions(cls, key):
        if key in cls.keyActionQueues:
            for action in cls.keyActionQueues[key]:
                action()

    @classmethod
    def registerActionToKey(cls, key, method):
        if cls.keyDefaultAction[key] == cls.keyActionQueues[key]:
            cls.keyActionQueues[key] = [method]
        else:
            cls.keyActionQueues[key].append(method)

    @classmethod
    def clearActionsOnKey(cls, key):
        cls.keyActionQueues[key] = cls.keyDefaultAction[key]

    @classmethod
    def setDefaultForKey(cls, key, default):
        cls.keyDefaultAction[key] = [default]
        if len(cls.keyActionQueues[key]) == 0:
            cls.keyActionQueues[key] = cls.keyDefaultAction[key]

    @classmethod
    def clearDefaultOnKey(cls, key):
        cls.keyDefaultAction[key] = []