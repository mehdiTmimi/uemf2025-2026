#!/usr/bin/env python3
"""
Desktop UI (Qt) to display the list of todos from the REST endpoint.
Endpoint: https://d483ba614525.ngrok-free.app/todos
"""
from urllib import request, error
import json
from typing import List, Dict, Any

from PySide6 import QtWidgets, QtCore

BASE_URL = "https://d483ba614525.ngrok-free.app"
ENDPOINT = "/todos"
URL = BASE_URL + ENDPOINT


def fetch_todos(url: str) -> List[Dict[str, Any]]:
    req = request.Request(url, headers={"Accept": "application/json"})
    try:
        with request.urlopen(req, timeout=15) as resp:
            status = resp.getcode()
            if status != 200:
                raise RuntimeError(f"Unexpected status code: {status}")
            data = resp.read().decode("utf-8")
            parsed = json.loads(data)
            # Accept both an array of todos or an object with a 'todos' property
            if isinstance(parsed, dict) and "todos" in parsed:
                todos = parsed["todos"]
            else:
                todos = parsed
            if not isinstance(todos, list):
                raise ValueError("Expected a list of todos")
            # Normalize structure: { id: str, task: str, completed: bool }
            normalized = []
            for t in todos:
                if not isinstance(t, dict):
                    continue
                normalized.append({
                    "id": str(t.get("id")),
                    "task": t.get("task", ""),
                    "completed": bool(t.get("completed", False)),
                })
            return normalized
    except error.HTTPError as e:
        raise SystemExit(f"HTTP error: {e.code} {e.reason}")
    except error.URLError as e:
        raise SystemExit(f"Connection error: {e.reason}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"Invalid JSON response: {e}")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, source_url: str):
        super().__init__()
        self.source_url = source_url
        self.setWindowTitle("Todos")
        self.resize(760, 480)

        central = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(central)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        # Header
        header = QtWidgets.QHBoxLayout()
        title = QtWidgets.QLabel("Todos")
        font = title.font()
        font.setPointSize(16)
        font.setBold(True)
        title.setFont(font)
        header.addWidget(title)
        header.addStretch(1)
        self.status_label = QtWidgets.QLabel(f"Source: {self.source_url}")
        header.addWidget(self.status_label)
        layout.addLayout(header)

        # Table
        self.table = QtWidgets.QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["ID", "Task", "Completed"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        layout.addWidget(self.table, 1)

        # Footer buttons
        footer = QtWidgets.QHBoxLayout()
        self.refresh_btn = QtWidgets.QPushButton("Refresh")
        self.refresh_btn.clicked.connect(self.refresh)
        footer.addWidget(self.refresh_btn)
        footer.addStretch(1)
        quit_btn = QtWidgets.QPushButton("Quit")
        quit_btn.clicked.connect(self.close)
        footer.addWidget(quit_btn)
        layout.addLayout(footer)

        self.setCentralWidget(central)

        # Initial load shortly after the UI shows
        QtCore.QTimer.singleShot(150, self.refresh)

    def set_status(self, text: str):
        self.status_label.setText(text)
        QtWidgets.QApplication.processEvents()

    def refresh(self):
        try:
            self.set_status("Loading…")
            todos = fetch_todos(self.source_url)
            self.table.setRowCount(0)
            for t in todos:
                row = self.table.rowCount()
                self.table.insertRow(row)
                self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(t.get("id", "")))
                self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(t.get("task", "")))
                completed_text = "Yes" if t.get("completed") else "No"
                self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(completed_text))
            self.set_status(f"Loaded {self.table.rowCount()} item(s) • Source: {self.source_url}")
        except SystemExit as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))
            self.set_status("Failed to load todos")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Unexpected error: {e}")
            self.set_status("Failed to load todos")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = MainWindow(URL)
    win.show()
    app.exec()
