Below are short Mermaid demos for each diagram class you mentioned. Each code block can be rendered by tools or platforms that support Mermaid.

***

### 1. Flowchart

```mermaid
flowchart TD
    A[Start] --> B{Is it sunny?}
    B -- Yes --> C[Go for a walk]
    B -- No --> D[Read a book]
    C --> E[Enjoy the day]
    D --> E
```

***

### 2. Sequence Diagram

```mermaid
sequenceDiagram
    participant Alice
    participant Bob
    Alice->>Bob: Hello, Bob!
    Bob-->>Alice: Hi, Alice!
    Alice->>Bob: How are you?
    Bob-->>Alice: I am good, thanks!
```

***

### 3. State Diagram

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing : event/start
    Processing --> Idle : event/stop
    Processing --> Error : event/fail
    Error --> Idle : retry
```

***

### 4. Entity-Relationship Diagram

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE_ITEM : contains
    CUSTOMER }|..|{ DELIVERY_ADDRESS : uses
```

***

### 5. Gantt Chart

```mermaid
gantt
    title Project Timeline
    dateFormat  YYYY-MM-DD
    section Planning
    Task A         :a1, 2025-08-18, 3d
    Task B         :after a1, 3d
    section Development
    Task C         :2025-08-25, 5d
```

***

### 6. Pie Chart

```mermaid
pie
    title Programming Language Usage
    "Python" : 45
    "JavaScript" : 25
    "Java" : 20
    "Other" : 10
```

***

Copy any of these blocks into a Mermaid-compatible environment to see them rendered as diagrams!

Sources
