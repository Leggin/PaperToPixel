set -a
source .env
streamlit run image_upload_page.py
python3 scanner_api.py