import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen

class DrawingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('paint 0')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: white;")
        
        self.drawing = False
        self.points = []
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.points.append([event.pos()])
    
    def mouseMoveEvent(self, event):
        if self.drawing:
            self.points[-1].append(event.pos())
            self.update()
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
    
    def paintEvent(self, event):
        if self.points:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.black, 2))
            
            for line in self.points:
                for i in range(1, len(line)):
                    painter.drawLine(line[i-1], line[i])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DrawingApp()
    window.show()
    sys.exit(app.exec_())