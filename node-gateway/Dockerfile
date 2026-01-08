# Use the official Node.js image
FROM node:18-slim

# Set the working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the node files
COPY . .

# Expose the port Node.js runs on
EXPOSE 3000

# Start the application
CMD ["node", "index.js"]