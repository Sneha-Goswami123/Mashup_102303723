
# 🎵 Mashup Generator Web Application  

A Python-based Web Service that generates a music mashup from YouTube videos of a specified singer and sends the final mashup to the user's email.

🔗 **Live Deployed Link:**  
[https://mashup-102303723.onrender.com](https://mashup-102303723.onrender.com)  

---

## 📌 Project Objective  

This project implements:

1. A Command-Line Mashup Generator  
2. A Web-Based Mashup Service  
3. Cloud Deployment of the Web Service  

The system automatically downloads videos, extracts audio, trims clips, merges them, and emails the final mashup to the user.

---

## ⚙️ Methodology  

### Step 1: User Input  
The user provides:
- Singer Name  
- Number of Videos (must be > 10)  
- Clip Duration in seconds (must be > 20)  
- Email ID  

### Step 2: Video Download  
- YouTube videos are fetched using `yt-dlp`.  
- Videos are downloaded programmatically.  

### Step 3: Audio Processing  
- Audio is extracted from downloaded videos.  
- Each clip is trimmed to the specified duration.  
- FFmpeg is used for audio handling and merging.  

### Step 4: Mashup Creation  
- All trimmed clips are concatenated into a single `.mp3` file.  

### Step 5: Email Delivery  
- Final output is compressed into a ZIP file.  
- File is sent to the user via Gmail SMTP using App Password authentication.  

### Step 6: Deployment  
- Hosted on Render Cloud Platform.  
- Gunicorn used as production server.  
- Environment variables used for secure credential storage.  

---

## 🛠️ Technologies Used  

- Python  
- Flask  
- yt-dlp  
- FFmpeg  
- MoviePy  
- Gunicorn  
- Render (Cloud Deployment)  

---

## 💻 How to Run Locally  

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:10000
```

---

## 📊 Results  

- Successfully generates mashup from multiple videos  
- Validates correct number of parameters  
- Displays appropriate messages for invalid input  
- Handles exceptions gracefully  
- Automatically emails final mashup  
- Fully deployed and accessible online  

---

## 🔐 Environment Variables  

The following environment variables are required:

```
email_user
email_pass
```

(App Password is used for Gmail SMTP authentication.)

---

## 👩‍💻 Author  

Sneha Goswami  
Roll No: 102303723  

