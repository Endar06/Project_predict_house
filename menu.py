import warnings
warnings.filterwarnings('ignore')
import streamlit as st 
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu('Pilih Halaman',
    ['Tentang Saya','Dashboard',
     'Proyek', 'Kontak'],                       
    default_index=0)
    
if selected == 'Proyek':
    import house
    house.house_predict()
elif selected == 'Kontak':
    import kontak
    kontak.tampilkan_kontak()
elif selected == 'Tentang Saya':
    import tentang
    tentang.tentang()
elif selected == 'Dashboard':
    import dashboard
    dashboard.house_dashboard()