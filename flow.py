# flow.py
from metaflow import FlowSpec, step

class HelloFlow(FlowSpec):

    @step
    def start(self):
        print("Step 1: Starting the flow...")
        self.name = "Shubham"
        self.next(self.greet)

    @step
    def greet(self):
        print(f"Step 2: Hello, {self.name}!")
        self.message = f"Welcome to Metaflow, {self.name}!"
        self.next(self.process)

    @step
    def process(self):
        print("Step 3: Doing some processing...")
        self.result = self.message.upper()
        self.next(self.end)

    @step
    def end(self):
        print("Step 4: Flow finished.")
        print("Final result:", self.result)

if __name__ == '__main__':
    HelloFlow()
