exports.config = {
  seleniumServerJar: 'node_modules/selenium-standalone/.selenium/2.43.1/server.jar',

  chromeDriver: 'node_modules/selenium-standalone/.selenium/2.43.1/chromedriver',

  capabilities: {
    'browserName': 'firefox'
  },

  jasmineNodeOpts: {
    showColors: true,
    defaultTimeoutInterval: 30000
  }
};
