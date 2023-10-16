CREATE TABLE projects
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE users
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    name     TEXT NOT NULL,
    email    TEXT NOT NULL,
    password TEXT NOT NULL
);


CREATE TABLE tasks
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT                                                     NOT NULL,
    status      TEXT CHECK ( status IN ('TODO', 'IN_PROGRESS', 'DONE') ) NOT NULL DEFAULT 'TODO',
    priority    TEXT CHECK ( priority IN ('LOW', 'MEDIUM', 'HIGH') )     NOT NULL DEFAULT 'MEDIUM',
    project_id  INTEGER                                                  NOT NULL,

    description TEXT,
    due_date    DATE,
    assignee_id INTEGER,

    FOREIGN KEY (assignee_id) REFERENCES users (id) ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE ON UPDATE CASCADE,
    CHECK ( case when status = 'DONE' then assignee_id is not null else 1 end )
);