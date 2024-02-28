# ALfaLLM
LLM for Alfa Bank
# Alfa Bank Test Assignment

This repository is dedicated to a test assignment for Alfa Bank, showcasing an integration of advanced machine learning techniques to enhance customer service and information processing within the banking domain. The project encompasses a set of scripts designed for various tasks, including data parsing, model fine-tuning, and deploying a responsive Telegram bot.

## Project Components

### Information Parser
- **Description**: A script developed for extracting specific information from the Alfa Bank website. This component plays a crucial role in gathering data that can be used for generating insightful responses and for training the machine learning model.

### Fine-Tuning Llama 2
- **Technique**: The project utilizes the Llama 2 model, which has been fine-tuned to improve its performance on banking-related queries. The fine-tuning process incorporates LoRA (Low-Rank Adaptation), allowing for effective model adaptation to the financial domain with minimal computational overhead.
- **Limitation**: Due to the constraints of computational resources, response generation is capped at 100 tokens. This ensures efficient and relevant output without exceeding the processing capabilities of the system.

### Telegram Bot
- **Functionality**: A Telegram bot equipped to answer user questions by leveraging the fine-tuned Llama 2 model hosted on Hugging Face. This bot facilitates real-time interactions, offering banking advice and information retrieval in a user-friendly manner.

## Demonstration
Below is an example of the bot in action, illustrating its ability to interact with users and provide accurate responses based on the fine-tuned model.

![Example of the bot in action](images/image.png)

## Overview
The aim of this project is to demonstrate the practical applications of state-of-the-art NLP technologies in the banking industry. By leveraging machine learning, we can significantly enhance the efficiency and effectiveness of customer service and information dissemination in the banking sector.
