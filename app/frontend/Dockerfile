# Stage 1: Build the React app
FROM node:16-alpine as build

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all files from the current directory to /app in the Docker image
COPY . .

# Build the React app
RUN npm run build

# Stage 2: Serve the React app with nginx
FROM nginx:stable-alpine

# Copy the built app from the previous stage
COPY --from=build /app/build /usr/share/nginx/html

# Copy nginx configuration to set up URL rewriting
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 to the outside world
EXPOSE 80

# Start nginx server
CMD ["nginx", "-g", "daemon off;"]

