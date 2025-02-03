from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    help = "This commands inserts post data"

    def handle(self,*args: Any, **options: Any):

        Post.objects.all().delete()
        
        titles = [
            "The Joy of Terrace Gardening",
            "5 Simple ReactJS Tips for Beginners",
            "Exploring the Beauty of Abstract Art",
            "Building a Full-Stack App with the MERN Stack",
            "The Ultimate Guide to Sketching for Beginners",
            "Healthy Recipes for a Busy Lifestyle",
            "Animating Your Website with Framer Motion",
            "How to Grow Tomatoes on Your Rooftop",
            "Why JavaScript is the King of Web Development",
            "10 Must-Visit Places in South India",
            "Mastering the Basics of Node.js",
            "Creating Responsive Layouts with Tailwind CSS",
            "Benefits of Practicing Yoga Daily",
            "Breaking Down the Basics of Machine Learning",
            "A Beginner’s Guide to Digital Marketing",
            "Understanding MongoDB Aggregations",
            "How to Paint Stunning Watercolor Landscapes",
            "Best Practices for Writing Clean Code",
            "Top 5 Tools for Developers in 2024",
            "The Importance of Mental Health Awareness"
        ]

        contents = [
            "Terrace gardening transforms unused rooftops into lush spaces for growing vegetables and flowers.",
            "Learn how ReactJS hooks simplify state management and event handling for dynamic web apps.",
            "Abstract art allows viewers to connect emotionally without relying on recognizable forms.",
            "The MERN stack is ideal for building modern web apps with seamless client-server integration.",
            "Sketching can be therapeutic and is a great skill for expressing creativity.",
            "Quick recipes ensure you stay healthy while managing a hectic schedule.",
            "Framer Motion adds elegance to web animations with ease.",
            "Tomatoes thrive in rooftop gardens with the right care and containers.",
            "JavaScript continues to dominate web development with its versatility.",
            "South India offers a rich cultural heritage and stunning landscapes.",
            "Node.js powers high-performance server-side applications with JavaScript.",
            "Tailwind CSS simplifies creating beautiful and responsive web designs.",
            "Daily yoga improves flexibility, balance, and mental clarity.",
            "Machine learning opens up opportunities for predictive analytics and automation.",
            "Digital marketing helps businesses thrive in the competitive online landscape.",
            "MongoDB's aggregation framework makes advanced data analysis a breeze.",
            "Watercolor painting techniques bring landscapes to life.",
            "Writing clean code reduces errors and improves collaboration.",
            "Modern development tools enhance productivity and collaboration.",
            "Mental health awareness breaks stigma and promotes better well-being."
        ]

        img_urls = [
            "https://images.pexels.com/photos/450516/pexels-photo-450516.jpeg",  # Terrace Gardening
            "https://images.pexels.com/photos/1181675/pexels-photo-1181675.jpeg",  # ReactJS Tips
            "https://images.pexels.com/photos/102127/pexels-photo-102127.jpeg",  # Abstract Art
            "https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg",  # MERN Stack
            "https://images.pexels.com/photos/1053687/pexels-photo-1053687.jpeg",  # Sketching Guide
            "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg",  # Healthy Recipes
            "https://images.pexels.com/photos/1181677/pexels-photo-1181677.jpeg",  # Framer Motion
            "https://images.pexels.com/photos/102104/pexels-photo-102104.jpeg",  # Growing Tomatoes
            "https://images.pexels.com/photos/1181264/pexels-photo-1181264.jpeg",  # JavaScript Web Dev
            "https://images.pexels.com/photos/1640778/pexels-photo-1640778.jpeg",  # South India Places
            "https://images.pexels.com/photos/1181265/pexels-photo-1181265.jpeg",  # Node.js Basics
            "https://images.pexels.com/photos/1181266/pexels-photo-1181266.jpeg",  # Tailwind Responsive
            "https://images.pexels.com/photos/1640779/pexels-photo-1640779.jpeg",  # Yoga Benefits
            "https://images.pexels.com/photos/1181267/pexels-photo-1181267.jpeg",  # Machine Learning
            "https://images.pexels.com/photos/1181268/pexels-photo-1181268.jpeg",  # Digital Marketing
            "https://images.pexels.com/photos/1181269/pexels-photo-1181269.jpeg",  # MongoDB Aggregations
            "https://images.pexels.com/photos/1181270/pexels-photo-1181270.jpeg",  # Watercolor Landscapes
            "https://images.pexels.com/photos/1181271/pexels-photo-1181271.jpeg",  # Clean Code
            "https://images.pexels.com/photos/1181272/pexels-photo-1181272.jpeg",  # Dev Tools 2024
            "https://images.pexels.com/photos/1181273/pexels-photo-1181273.jpeg"   # Mental Health Awareness
]

        categories = Category.objects.all()
        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
