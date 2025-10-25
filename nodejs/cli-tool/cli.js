#!/usr/bin/env node
import { Command } from 'commander';
import chalk from 'chalk';
import ora from 'ora';
import inquirer from 'inquirer';
import dotenv from 'dotenv';

dotenv.config();

const program = new Command();

program
  .name('mycli')
  .description('A sample CLI application')
  .version('1.0.0');

program
  .command('hello')
  .description('Say hello')
  .option('-n, --name <name>', 'Name to greet', 'World')
  .action((options) => {
    console.log(chalk.green(`Hello, ${options.name}!`));
  });

program
  .command('init')
  .description('Initialize the application')
  .action(async () => {
    const spinner = ora('Initializing application...').start();
    
    // Simulate some work
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    spinner.succeed('Initialization complete!');
    
    const answers = await inquirer.prompt([
      {
        type: 'input',
        name: 'projectName',
        message: 'What is your project name?',
        default: 'my-project'
      },
      {
        type: 'confirm',
        name: 'confirm',
        message: 'Do you want to continue?',
        default: true
      }
    ]);
    
    if (answers.confirm) {
      console.log(chalk.blue(`Creating project: ${answers.projectName}`));
      console.log(chalk.green('✓ Project created successfully!'));
    } else {
      console.log(chalk.yellow('Operation cancelled.'));
    }
  });

program
  .command('run')
  .description('Run the main task')
  .option('-v, --verbose', 'Verbose output')
  .action((options) => {
    const spinner = ora('Running main task...').start();
    
    if (options.verbose) {
      spinner.info('Verbose mode enabled');
    }
    
    // Simulate some work
    setTimeout(() => {
      spinner.succeed('Task completed!');
    }, 2000);
  });

program.parse();
