 
# Cardistry Move Organiser
## A personal desktop application designed to help cardists catalogue, categorize, and track progress on every move, flourish, and cut they learn.
Built using **Python** with the built in ```tkinter``` library for the GUI, ```SQLite``` for a database , user authentication and data management.

---
## Installation and Setup

### Prerequisites

* You must have **Python 3.x** installed on your system.
* *Note: This application uses built-in Python libraries (Tkinter for GUI and SQLite for the database), so no extra installations are required!*

### 1. Clone the Repository

```bash
git clone https://github.com/mheathcock/Cardistry-Move-Organiser.git
cd Cardistry-Move-Organiser
```
### 2. Run the Application

Execute the main Python file to start the desktop application:

```bash
python main.py
```
---

## Development Roadmap

This section tracks current progress and outlines future goals for the application.

### Phase 1: Core Functionality (Current Focus)

| Feature Area | Task | Status |
| :--- | :--- | :--- |
| **Authentication (Backend)** | Account Database Setup | [X] Done |
| | Account Authorization Logic | [X] Done |
| **GUI (Skeleton)** | Login / Register Interface | [X] Done |
| | Video Database Viewing | [X] Done |
| | Video Viewing / Notes Interface | [ ] To Do |
| **Data (Skeleton)** | Video Storage / Retrieval | [X] Done |
| **Data (Refined)** | Video Storage / Retrieval Polish | [ ] To Do |

---

### Phase 2: User Interface Refinement

Focus is on polishing the user experience with production-ready GUIs:

* **Polished GUI** for Account Login / Register
* **Polished GUI** for Video Upload
* **Polished GUI** for Video Database
* **Polished GUI** for Video Viewing / Notes

---

### Phase 3: Advanced Functionality (Future Development)

To be implemented once core features are stable:

* **Progress Tracking System:** Allow users to mark moves as ***Learning***, ***Mastered***, or ***Archived***.
* **Categorization Logic:** Implement backend and frontend logic to assign and filter moves by key categories:
    * **Primary Categories:** **Packet Cuts**, **Fans**, **Isolations**, etc.
    * **Sub-categories:** **One Handed**, **Two Handed**, **Body**, etc.
* **Search Functionality:** Implement a robust search feature for move names and notes.
* **Embedded Video Player:** Integrate a dedicated player directly within the application interface.
