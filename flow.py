# flow.py
from metaflow import FlowSpec, step

class HelloFlow(FlowSpec):

    @step
    def start(self):
        print("Hello, to shubham's world!")
        self.next(self.end)

    @step
    def end(self):
        print("Flow finished.")

if __name__ == '__main__':
    HelloFlow()

