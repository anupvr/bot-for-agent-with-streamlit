import subprocess
import os

def launch_streamlit_bot():
    try:
        print("🚀 Starting ProductBot UI (Streamlit)...")
        subprocess.run(["streamlit", "run", "product_bot.py"])
    except KeyboardInterrupt:
        print("🛑 Stopped by user.")
    except Exception as e:
        print(f"❌ Error launching Streamlit: {e}")

if __name__ == "__main__":
    launch_streamlit_bot()