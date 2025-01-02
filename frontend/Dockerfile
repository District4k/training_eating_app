# Use a more recent Node.js version
FROM node:18-alpine

# Set working directory
WORKDIR /opt/app/frontend

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Add node_modules to PATH
ENV PATH ./node_modules/.bin:$PATH

# Copy application code
COPY . .

# Build for production
#RUN npm run build

# Expose port
EXPOSE 8080

# Start the app
CMD ["npm", "run", "serve"]
