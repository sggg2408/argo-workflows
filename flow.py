# flow.py
from metaflow import FlowSpec, step

class HelloFlow(FlowSpec):

    @step
    def start(self):
        print("Hello, world!")
        self.next(self.end)

    @step
    def end(self):
        print("Flow finished.")

if __name__ == '__main__':
    HelloFlow()

