VRTS_uconnect_hackathon_2024

To compile the code in the machine, follow these steps:
1. Configure the environment for code execution.
2. Execute the `PermissionWindow.py` file from the `Final upload` folder.
3. Dismiss each pop-up window for the graphs to proceed with the program.
   
The background processes consist of four command prompts that operate inconspicuously. Notifications for the user will be exclusively provided through pop-up messages.
In the matrix, a value of 1 signifies normal behavior, while -1 indicates anomalies. Specifically, pop-up notifications will be generated for -1 values associated with CPU and disk events.

Demo Video Link: [https://drive.google.com/file/d/1utAWGlnsi4t9RZffXebrx6iZHcsX_BLH/view?usp=drive_link](url)



> Key points:

**Complete Real Time Application**- The application collects actual parameters of the system and feeds to the model. The user can monitor anomalous behavior of system real time.

**Constant Improvement** The application uses supervised modeling for network, This is constantly updating the training data to refine the model gradually. After generating an output, the collected data and prediction is added to the training set. This iterative approach ensures the ongoing improvement of our model.

**Multithreading** for multiple programs to run simultaneously. Detection for network and hardware (cpu, disk work in parallel).
Since the program is running continuously in the background, detection for each should be continuously done in parallel. ->Lightweight application

