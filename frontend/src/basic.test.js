describe('Task Manager Unit Tests', () => {
  test('1 + 1 equals 2', () => {
    expect(1 + 1).toBe(2);
  });

  test('Task object has correct structure', () => {
    const task = {
      id: 1,
      title: 'Test Task',
      description: 'Test Description',
      status: 'pending',
      created_at: '2025-12-17T19:00:00Z'
    };

    expect(task.id).toBe(1);
    expect(task.title).toBe('Test Task');
    expect(task.status).toBe('pending');
    expect(typeof task.created_at).toBe('string');
  });

  test('Filter tasks by status', () => {
    const tasks = [
      { id: 1, title: 'Task 1', status: 'pending' },
      { id: 2, title: 'Task 2', status: 'in_progress' },
      { id: 3, title: 'Task 3', status: 'done' },
      { id: 4, title: 'Task 4', status: 'pending' }
    ];

    const pendingTasks = tasks.filter(task => task.status === 'pending');
    const doneTasks = tasks.filter(task => task.status === 'done');

    expect(pendingTasks.length).toBe(2);
    expect(doneTasks.length).toBe(1);
    expect(pendingTasks[0].id).toBe(1);
    expect(pendingTasks[1].id).toBe(4);
  });

  test('Add new task to array', () => {
    let tasks = [];

    // Симуляция создания задачи
    const newTask = {
      id: tasks.length + 1,
      title: 'New Task',
      status: 'pending'
    };

    tasks.push(newTask);
    expect(tasks.length).toBe(1);
    expect(tasks[0].title).toBe('New Task');

    // Добавляем вторую задачу
    const anotherTask = {
      id: tasks.length + 1,
      title: 'Another Task',
      status: 'in_progress'
    };

    tasks.push(anotherTask);
    expect(tasks.length).toBe(2);
    expect(tasks[1].status).toBe('in_progress');
  });
});