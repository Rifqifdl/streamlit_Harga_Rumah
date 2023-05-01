import pickle
import streamlit as st

model = pickle.load(open('estimasi_rumahdiparis.sav','rb'))

st.title('Estimasi Harga Rumah di Paris')

squareMeters = st.number_input('Input Luas Lahan')
numberOfRooms = st.number_input('Input Jumlah Ruangan')
floors = st.number_input('Input Jumlah Lantai')
numPrevOwners = st.number_input('Input Jumlah Pemilik Yang Pernah Menempati')
basement = st.number_input('Input Luas Basement')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[squareMeters, numberOfRooms, floors, numPrevOwners, basement]]
    )
    st.write ('Estimasi harga rumah dalam Dollar : ', predict)
    st.write ('Estimasi harga rumah dalam IDR (Juta) :', predict*15000)