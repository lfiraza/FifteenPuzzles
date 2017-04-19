from PyQt5 import QtGui, QtCore, QtWidgets

class MainWindow(QtWidgets.QMainWindow):

    itemAnimationFinished = QtCore.pyqtSignal()

    def __init__(self, nrows, ncols, init_data, SPACER, puzzle_solution):
        super(MainWindow, self).__init__()

        self.nrows = nrows
        self.ncols = ncols
        self.init_data = init_data
        self.block_array = []
        self.SPACER = SPACER
        self.spacer_pos = self.find_spacer()
        self.puzzle_solution = puzzle_solution
        self.puzzle_solution_bak = puzzle_solution

        self.animationSlideTimer = QtCore.QTimer(self)
        self.animationDelayTimer = QtCore.QTimer(self)
        self.animationSlideTimer.setInterval(10)
        self.animationDelayTimer.setInterval(500)
        self.animated_item = None                       # qgraphics item
        self.animated_pos_diff = None                   # dx, dy
        self.animated_finish_pos = None                 # target position where animation stops

        self.gv = QtWidgets.QGraphicsView()
        self.gv.setFixedSize(ncols * 100 + 10, nrows * 100 + 10)

        self.setFixedSize(self.sizeHint())
        self.solveButton = QtWidgets.QPushButton("Solve")

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.addWidget(self.gv)
        self.mainLayout.addWidget(self.solveButton)
        self.setCentralWidget(QtWidgets.QWidget())
        self.centralWidget().setLayout(self.mainLayout)
        self.setWindowTitle("15Puzzles")


        gvRect = self.gv.rect()
        gvRect.setSize(QtCore.QSize(gvRect.width(), gvRect.height()))
        self.scene = QtWidgets.QGraphicsScene(QtCore.QRectF(gvRect), self.gv)
        self.gv.setScene(self.scene)

        self.rcontent = self.gv.contentsRect();
        self.gv.setSceneRect(0, 0, self.rcontent.width(), self.rcontent.height());

        self.solveButton.clicked.connect(self.solve_visually)
        self.animationSlideTimer.timeout.connect(self.animate)
        self.animationDelayTimer.timeout.connect(self.solve_visually)
        self.itemAnimationFinished.connect(self.animationDelayTimer.start)

        self.create_blocks()
        self.fillData()

    def create_blocks(self):
        """
        Creates block rectangles and adds them to scene.
        """
        for i in range(self.nrows):
            line_block = []
            for j in range(self.ncols):
                block = QtWidgets.QGraphicsRectItem(0, 0, 100, 100)
                block.setPos(j * 100, i * 100)
                self.scene.addItem(block)
                line_block.append(block)

            self.block_array.append(line_block)

    def fillData(self):
        """
        Fill puzzle blocks with numbers and remove SPACER block.
        Fills puzzle block with color - zigzag
        """
        color1 = QtCore.Qt.lightGray
        color2 = QtCore.Qt.gray
        last_color = color1
        color_table = {}

        # generate dict with color for each number (1-lgray, 2-gray, 3-lgray, etc.)
        keys = range(self.nrows*self.ncols)
        for key in keys:
            color_table[key] = last_color
            last_color = color1 if last_color == color2 else color2

        for j in range(self.ncols):
            for i in range(self.nrows):
                block = self.block_array[i][j]
                blockBoundRect = block.boundingRect()

                num = self.init_data[i][j]
                if num == self.SPACER:
                    self.scene.removeItem(block)
                    continue
                else:
                    text = str(num)
                    block.setBrush(QtGui.QColor(color_table[num]))

                textItem = QtWidgets.QGraphicsSimpleTextItem(text, block)
                font = textItem.font()
                font.setPixelSize(50)
                textItem.setFont(font)
                textItemBoundRect = textItem.boundingRect()
                new_x = blockBoundRect.width() / 2.0 - textItemBoundRect.width() / 2.0
                new_y = blockBoundRect.height() / 2.0 - textItemBoundRect.height() / 2.0
                textItem.setPos(new_x, new_y)

    def find_spacer(self):
        for ii in range(self.nrows):
            for jj in range(self.ncols):
                if self.init_data[ii][jj] == self.SPACER:
                    return ii, jj

        raise Exception("ERROR. SPACER not found in %s" % self.init_data)

    def finished(self):
        self.solveButton.setText("It's sorted!")
        self.solveButton.setEnabled(False)

    @QtCore.pyqtSlot()
    def solve_visually(self):
        self.animationDelayTimer.stop()

        if not self.puzzle_solution:
            self.finished()
            return

        next_move = self.puzzle_solution[-1]
        del self.puzzle_solution[-1]

        spacer_x, spacer_y = self.spacer_pos

        if next_move == 'P':
            self.block_array[spacer_x][spacer_y + 1], self.block_array[spacer_x][spacer_y] = self.block_array[spacer_x][spacer_y], self.block_array[spacer_x][spacer_y + 1]
            self.animated_item = self.block_array[spacer_x][spacer_y]
            self.animated_pos_diff = QtCore.QPointF(-10, 0)
            self.animated_finish_pos = QtCore.QPointF(spacer_y * 100, spacer_x * 100)
            self.spacer_pos = (spacer_x, spacer_y + 1)

        elif next_move == 'D':
            self.block_array[spacer_x + 1][spacer_y], self.block_array[spacer_x][spacer_y] = self.block_array[spacer_x][spacer_y], self.block_array[spacer_x + 1][spacer_y]
            self.animated_item = self.block_array[spacer_x][spacer_y]
            self.animated_pos_diff = QtCore.QPointF(0, -10)
            self.animated_finish_pos = QtCore.QPointF(spacer_y * 100, spacer_x * 100)
            self.spacer_pos = (spacer_x + 1, spacer_y)

        elif next_move == 'L':
            self.block_array[spacer_x][spacer_y - 1], self.block_array[spacer_x][spacer_y] = self.block_array[spacer_x][spacer_y], self.block_array[spacer_x][spacer_y - 1]
            self.animated_item = self.block_array[spacer_x][spacer_y]
            self.animated_pos_diff = QtCore.QPointF(10, 0)
            self.animated_finish_pos = QtCore.QPointF(spacer_y * 100, spacer_x * 100)
            self.spacer_pos = (spacer_x, spacer_y - 1)

        elif next_move == 'G':
            self.block_array[spacer_x - 1][spacer_y], self.block_array[spacer_x][spacer_y] = self.block_array[spacer_x][spacer_y], self.block_array[spacer_x - 1][spacer_y]
            self.animated_item = self.block_array[spacer_x][spacer_y]
            self.animated_pos_diff = QtCore.QPointF(0, 10)
            self.animated_finish_pos = QtCore.QPointF(spacer_y * 100, spacer_x * 100)
            self.spacer_pos = (spacer_x - 1, spacer_y)

        self.animationSlideTimer.start()

    @QtCore.pyqtSlot()
    def animate(self):
        current_pos = self.animated_item.pos()

        if current_pos == self.animated_finish_pos:
            self.animationSlideTimer.stop()
            self.itemAnimationFinished.emit()
        else:
            newPos = current_pos + self.animated_pos_diff
            self.animated_item.setPos(newPos)


