import pickle
import streamlit as st

model = pickle.load(open('estimasi_rumahdiparis.sav','rb'))

st.title('Estimasi Harga Rumah di Paris')

squareMeters = st.number_input('Input Luas Lahan (Meter Persegi)')
numberOfRooms = st.number_input('Input Jumlah Ruangan')
floors = st.number_input('Input Jumlah Lantai')
numPrevOwners = st.number_input('Input Jumlah Pemilik Yang Pernah Menempati')
basement = st.number_input('Input Luas Basement (Meter Persegi)')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[squareMeters, numberOfRooms, floors, numPrevOwners, basement]]
    )
    st.write ('Estimasi harga rumah dalam EUR : ', predict)
    st.write ('Estimasi harga rumah dalam IDR :', predict*15000)
