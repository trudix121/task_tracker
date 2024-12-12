<h1>Task Tracker CLI Project</h1>
<h2>Introduction</h2>
<p>This is a simple <strong>task tracker CLI project</strong> built using <a href="https://www.python.org/">Python</a> and the <a href="https://click.palletsprojects.com/">Click library</a>. The program allows users to manage their tasks by adding, updating, removing, and marking them as done or in progress.</p>

<h2>Running the Program</h2>
<p>To run the program, use the following commands:</p> <ul> <li><strong>Windows:</strong> <code>py app.py</code></li> <li><strong>Linux:</strong> <code>python3 app.py</code></li> </ul>

<h2>Available Commands</h2>
<p>The program supports the following commands:</p> <ul> <li><code>add &lt;name&gt;</code>: Add a new task with the given name.</li> <li><code>update &lt;id&gt; &lt;new_desc&gt;</code>: Update the description of the task with the given ID.</li> <li><code>remove &lt;id&gt;</code>: Remove the task with the given ID.</li> <li><code>mark_done &lt;id&gt;</code>: Mark the task with the given ID as done.</li> <li><code>mark_in_progress &lt;id&gt;</code>: Mark the task with the given ID as in progress.</li> <li><code>list</code>: Show all tasks. You can also filter tasks by status by using the <code>done</code> or <code>to-do</code> argument.</li> </ul>

<h2>Examples</h2>
<p>Here are some examples of how to use the program:</p> <ul> <li><code>add "Buy milk"</code>: Add a new task to buy milk.</li> <li><code>update 1 "Buy eggs"</code>: Update the description of the task with ID 1 to "Buy eggs".</li> <li><code>remove 2</code>: Remove the task with ID 2.</li> <li><code>mark_done 1</code>: Mark the task with ID 1 as done.</li> <li><code>list</code>: Show all tasks.</li> <li><code>list done</code>: Show only tasks that are marked as done.</li> <li><code>list to-do</code>: Show only tasks that are marked as to-do.</li> </ul>

<h2>Versions</h2>
<p>This program has two versions available:</p> <ul> <li>One version uses only default <a href="https://www.python.org/">Python</a> libraries.</li> <li>One version uses the <a href="https://click.palletsprojects.com/">Click library</a> for building the CLI.</li> </ul>

<h2>Note</h2>
<p>Please make sure to use the correct version of the program according to your needs. If you have any issues or questions, feel free to ask.</p