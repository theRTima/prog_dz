import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem



class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('table')
        self.setGeometry(100, 100, 500, 300)
        
        layout = QVBoxLayout()
        
        data = [
            ['half-life 2', '2004','FPS'],
            ['EFT', '2025','FPS'],
            ['Dispatch', '2025','text-based'],
            ['EFT', '2025','FPS'],
            ['Dispatch', '2025','text-based'],
        ]

        table = QTableWidget()
        table.setRowCount(5)
        table.setColumnCount(3)
        
        table.setHorizontalHeaderLabels(['game', 'release_date'])
        
        
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                table.setItem(row, col, QTableWidgetItem(value))
        
        layout.addWidget(table)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Table()
    window.show()
    sys.exit(app.exec_())