import streamlit as st

def tampilkan_kontak():
    st.title("📞 Kontak Saya")

    st.subheader("Silakan hubungi Saya melalui informasi berikut:")

    st.markdown("""
    📍 *Alamat*: Bogor, Jawa Barat

    📧 *Email*: endardwi507@gmail.com  

    📱 *Telepon/WA*: +62 822-4947-2469  
    """)

    with st.form("form_kontak"):
        nama = st.text_input("Nama Anda")
        email = st.text_input("Email")
        pesan = st.text_area("Pesan")

        submit = st.form_submit_button("Kirim")

        if submit:
            st.success(f"Terima kasih {nama}, pesan Anda sudah terkirim!")