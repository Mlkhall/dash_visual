import os
import sys
import plotly
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from plotly.graph_objects import Figure, Scatter


class DjgMain(QMainWindow):
    def __init__(self):
        super().__init__()

        # some example data
        x = np.arange(1000)
        y = x ** 2

        # create the plotly figure
        fig = Figure(Scatter(x=x, y=y))

        # we create html code of the figure
        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        self.setCentralWidget(plot_widget)

        self.resize(1600, 900)
        self.move(100, 100)

        self.group_box = QGroupBox('Группа кнопок', self)
        self.group_box.resize(300, 900)

        self.btn = QPushButton('Загрузить таблицы', self.group_box)
        self.btn.move(60, 40)
        self.btn.setFixedSize(150, 40)
        self.btn.clicked.connect(self.get_files_xlsx)

    def evt_btn_clicked(self):
        res = QMessageBox.question(self, 'Disk full', 'Your disk drive is almost full')
        if res == QMessageBox.Yes:
            QMessageBox.information(self, '', 'Yes')

    def evt_btn_get_text(self):
        res = QInputDialog.getText(self, 'Title', 'Inter your name:')
        print(res)

    def evt_btn_set_color(self):
        color = QColorDialog.getColor(QColor('#FF0000'), self, 'Choose Color')
        print(color)

    def get_files_xlsx(self):
        file = QFileDialog.getExistingDirectory(self, "Выберете папку")

        print(os.listdir(file)) if not file == '' else None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DjgMain()
    dlgMain.setWindowTitle('DOPER')
    dlgMain.show()

    sys.exit(app.exec_())
