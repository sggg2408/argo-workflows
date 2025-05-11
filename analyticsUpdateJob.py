from metaflow import FlowSpec, step

class AnalyticsUpdateJob(FlowSpec):

    @step
    def start(self):
        print("Starting analytics update job")
        self.data = [1, 2, 3]
        self.next(self.process)

    @step
    def process(self):
        print("Processing data")
        self.result = [x * 2 for x in self.data]
        self.next(self.end)

    @step
    def end(self):
        print("Job complete. Result:", self.result)

if __name__ == '__main__':
    AnalyticsUpdateJob()
