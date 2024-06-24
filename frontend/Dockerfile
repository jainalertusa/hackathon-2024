# Use an official Node runtime as a parent image
FROM node:16

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire project directory to the working directory
COPY . .

# Build your app
RUN npm run build

# Expose port 3000 to the outside world
EXPOSE 3000

# Serve the app
CMD ["npm", "start"]