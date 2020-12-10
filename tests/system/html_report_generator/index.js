const reporter = require('cucumber-html-reporter');
const { argv } = require('yargs')
  .demandOption(['inputFile', 'outputFile', 'browser'])
const {
  inputFile,
  outputFile,
  browser,
} = argv;
const options = {
  name: 'Docker Example',
  brandTitle: 'SYSTEM Test',
  theme: "bootstrap",
  jsonFile: inputFile,
  output: outputFile,
  reportSuiteAsScenarios: true,
  scenarioTimestamp: true,
  launchReport: false,
  metadata: {
    Browser: browser,
  }
};
reporter.generate(options);
