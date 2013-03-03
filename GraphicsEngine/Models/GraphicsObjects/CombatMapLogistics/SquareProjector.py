import ogre.renderer.OGRE as ogre

class SquareProjector(object):
    """Defines the map block selector square projector."""

    # Class Variables--------------------------------------------------------------------------------------------------#
    NO_TYPE=0
    MOVE_BOX=1
    ATTACK_BOX=2
    TARGET_BOX=3

    MOVE_PROJECTION="Blue_Box.png"
    ATTACK_PROJECTION="Red_Box.png"
    TARGET_PROJECTION="Yellow_Box.png"

    PROJECTOR_NODE_NAME_PREFIX = 'ProjectorNode'
    FILTER_NODE_NAME_PREFIX = 'FilterNode'
    FILTER="decal_filter.png"
    # -----------------------------------------------------------------------------------------------------------------#

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, sceneManagerIn, rootNode, rowIndex, columnIndex):
        """Creates the projector object.

        Required Parameters:
        sceneManagerIn -
        rootNode -
        rowIndex -
        columnIndex -
        """
        self.sceneManager = sceneManagerIn
        self.root = rootNode
        self.row = rowIndex
        self.column = columnIndex
        self.visible = False
        self.projectionNode = None
        self.projectionImage = None
        self.projectionFrustum = None
        self.filterFrustum = None
        self.filterNode = None
        self.filterImage = None
        self.mapBlock = None
        self.usedPasses = None
        self.projectionType = None

    # Initialises the projector to its starting position and projection------------------------------------------------#
    def initialise(self, xpos, ypos, namePrefix=''):
        """Initialises the projector. Sets position and images.

        Required Parameters:
        xpos -
        ypos -
        projection -
        filter -
        """
        # Set the default projection image
        self.filterImage = self.FILTER

        # Sets the projector to off as default
        self.visible = False
        self.projectionType = self.NO_TYPE

        # Creates the frustum projector
        self.projectionFrustum = ogre.Frustum()
        # Forces the projections to maintain a constant size
        self.projectionFrustum.setProjectionType(ogre.PT_ORTHOGRAPHIC)
        self.projectionFrustum.setOrthoWindowWidth(2.75)
        self.projectionFrustum.setAspectRatio(1)

        # Create a node and attach the projector
        self.projectionNode = self.root.createChildSceneNode("{0} {1!s}:{2!s} {3!s}".format(self.PROJECTOR_NODE_NAME_PREFIX, self.row, self.column, namePrefix))
        self.projectionNode.attachObject(self.projectionFrustum)
        self.projectionNode.setPosition(xpos, 10, ypos)
        self.projectionNode.lookAt(ogre.Vector3(xpos, 0, ypos), ogre.Node.TransformSpace.TS_PARENT)

        # Creates the reverse image filter projector
        self.filterFrustum = ogre.Frustum()
        self.filterFrustum.setProjectionType(ogre.PT_ORTHOGRAPHIC)
        self.filterFrustum.setOrthoWindowWidth(2.75)
        self.filterFrustum.setAspectRatio(1)
        self.filterNode = self.projectionNode.createChildSceneNode("{0} {1!s}:{2!s} {3!s}".format(self.FILTER_NODE_NAME_PREFIX, self.row, self.column, namePrefix))
        self.filterNode.attachObject(self.filterFrustum)
        self.filterNode.setOrientation(ogre.Quaternion(ogre.Radian(ogre.Degree(90)), ogre.Vector3(0,1,0)))

    # Ties the projector to a Map Block--------------------------------------------------------------------------------#
    def tieToMapBlock(self, mapBlockIn):
        self.mapBlock = mapBlockIn

    # Frees the projector from its Map Block---------------------------------------------------------------------------#
    def untieMapBlock(self):
        self.mapBlock = None

    # Modifies a Map Block to receive the projectors projection--------------------------------------------------------#
    def makeBlockReceiveProjection(self):
        # Enable the materials to receive the projections
        if self.usedPasses is None:
            self.usedPasses = {}
            for i in range(self.mapBlock.entity.getNumSubEntities()):
                blockMaterialName = self.mapBlock.entity.getSubEntity(i).getMaterialName()
                self.makeMaterialReceiveProjection(self.projectionImage, self.filterImage, blockMaterialName, self.projectionFrustum, self.filterFrustum)
        else:
            raise Exception('Cannot add projection to texture because a projection is already set on the given texture.')

    # Modifies a material to receive projection------------------------------------------------------------------------#
    def makeMaterialReceiveProjection(self, decalName, filterName, materialName, projectionFrustum, filterFrustum):
        """Modifies a material so that it can receive a projection, if a projection is not set already.

        Required Parameters:
        decalName - name of the image file that will be displayed on the material
        filterName - name of the filter file that will be filtering the image
        materialName - name of the material to modify
        frustumPair - the ( projection frustum, filter frustum ) pair which projects the images
        """

        # Get the material and create a new pass
        mat = ogre.MaterialManager.getSingleton().getByName(materialName)
        passer = mat.getTechnique(0).createPass()

        # Set the scene blending so that we don't get smears at the edge of our texture, as well as some additional options
        passer.setSceneBlending(ogre.SBT_TRANSPARENT_ALPHA)
        passer.setDepthBias(1)
        passer.setLightingEnabled(False)

        # Required to allow the projection to appear on the desired texture
        texState = passer.createTextureUnitState(decalName)
        # Allows the image from the specified frustum to appear on texture
        texState.setProjectiveTexturing(True, projectionFrustum)
        texState.setTextureAddressingMode(ogre.TextureUnitState.TAM_CLAMP)
        texState.setTextureFiltering(ogre.FO_POINT, ogre.FO_LINEAR, ogre.FO_NONE)

        # Filters the projection so there is no reverse projection
        texState = passer.createTextureUnitState(filterName)
        # Allows the filter from the specified frustum to appear on texture
        texState.setProjectiveTexturing(True, filterFrustum)
        texState.setTextureAddressingMode(ogre.TextureUnitState.TAM_CLAMP)
        texState.setTextureFiltering(ogre.TFO_NONE)

        # Stores the pass so it can be switched out later
        listing = self.usedPasses.get(materialName, [])
        listing.append(passer)
        self.usedPasses[materialName] = listing

    # Removes current projection capability from the Map Block---------------------------------------------------------#
    def removeProjectionFromBlock(self):
        # Remove the pass from the material
        if self.usedPasses is not None:
            for material in self.usedPasses:
                for passer in self.usedPasses[material]:
                    passer.getParent().removePass(passer.getIndex())
            self.usedPasses = None
        else:
            raise Exception('Cannot remove projection from texture because a projection is not set on the given texture.')

    # Make the projection visible--------------------------------------------------------------------------------------#
    def show(self):
        if not self.visible and self.projectionType is not self.NO_TYPE:
            self.visible = True
            self.makeBlockReceiveProjection()

    # Hide the projection----------------------------------------------------------------------------------------------#
    def hide(self):
        if self.visible:
            self.visible = False
            self.removeProjectionFromBlock()

    # Set the projection and filter image------------------------------------------------------------------------------#
    def setProjectionType(self, projectionType):
        if not self.visible:
            if projectionType == self.NO_TYPE:
                self.projectionImage = None
            elif projectionType == self.MOVE_BOX:
                self.projectionImage = self.MOVE_PROJECTION
            elif projectionType == self.ATTACK_BOX:
                self.projectionImage = self.ATTACK_PROJECTION
            elif projectionType == self.TARGET_BOX:
                self.projectionImage = self.TARGET_PROJECTION
            else:
                raise Exception("Specified Projection Type does not exist.")
            self.projectionType = projectionType
        else:
            raise Exception("Cannot change Projector's projection type because it is visible")

    def getProjectionType(self):
        return self.projectionType

    # Returns the position of the block that the projector is over-----------------------------------------------------#
    def getPosition(self):
        return self.row, self.column

    # Returns true if the selector is visible, else false--------------------------------------------------------------#
    def isVisible(self):
        return self.visible

    # Sets the position of the projector-------------------------------------------------------------------------------#
    def setPosition(self, xpos, ypos):
        self.projectionNode.setPosition(xpos, 10, ypos)
        self.filterNode.setPosition(xpos, 10, ypos)

    # Releases any used resources--------------------------------------------------------------------------------------#
    def cleanUp(self):
        self.projectionNode.detachAllObjects()
        self.filterNode.detachAllObjects()
        del self.projectionFrustum
        del self.filterFrustum
        self.sceneManager.destroySceneNode(self.projectionNode)
        self.sceneManager.destroySceneNode(self.filterNode)
        del self.projectionNode
        del self.filterNode
        self.mapBlock = None
        self.root = None
        self.sceneManager = None
