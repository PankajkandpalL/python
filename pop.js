import React, { useState } from 'react';
import { Modal, View, Text, TouchableOpacity, StyleSheet, Pressable } from 'react-native';

const PaymentModal = ({ visible, onClose, onPay }) => {
  const [walletOption, setWalletOption] = useState('PL Wallet');
  const [gatewayOption, setGatewayOption] = useState('Plur');

  return (
    <Modal
      visible={visible}
      animationType="slide"
      transparent
      onRequestClose={onClose}
    >
      <View style={styles.overlay}>
        <View style={styles.modal}>
          <Text style={styles.title}>Choose Payment Mode</Text>

          <Text style={styles.section}>Wallet</Text>
          {['PL Wallet', 'PL Currency'].map(option => (
            <TouchableOpacity
              key={option}
              style={styles.optionRow}
              onPress={() => setWalletOption(option)}
            >
              <View style={[styles.colorBox, {
                backgroundColor: option === 'PL Wallet' ? 'green' : 'orange'
              }]} />
              <Text style={styles.optionText}>{option}</Text>
              <Text style={styles.credit}>₹100.00</Text>
              <View style={styles.radioCircle}>
                {walletOption === option && <View style={styles.selectedRb} />}
              </View>
            </TouchableOpacity>
          ))}

          <Text style={styles.section}>Payment gateway</Text>
          {['Plur', 'Pay U'].map(option => (
            <TouchableOpacity
              key={option}
              style={styles.optionRow}
              onPress={() => setGatewayOption(option)}
            >
              <Text style={styles.optionText}>{option}</Text>
              <View style={styles.radioCircle}>
                {gatewayOption === option && <View style={styles.selectedRb} />}
              </View>
            </TouchableOpacity>
          ))}

          <Pressable style={styles.payButton} onPress={onPay}>
            <Text style={styles.payText}>Pay</Text>
          </Pressable>
        </View>
      </View>
    </Modal>
  );
};

export default PaymentModal;


const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.4)',
    justifyContent: 'flex-end',
  },
  modal: {
    backgroundColor: 'white',
    padding: 20,
    borderTopRightRadius: 15,
    borderTopLeftRadius: 15,
  },
  title: {
    fontSize: 18,
    fontWeight: '600',
    marginBottom: 10,
  },
  section: {
    fontSize: 14,
    fontWeight: '500',
    marginTop: 20,
    marginBottom: 10,
  },
  optionRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 15,
  },
  colorBox: {
    width: 12,
    height: 12,
    borderRadius: 2,
    marginRight: 10,
  },
  optionText: {
    flex: 1,
    fontSize: 16,
  },
  credit: {
    fontSize: 14,
    color: 'gray',
    marginRight: 10,
  },
  radioCircle: {
    height: 20,
    width: 20,
    borderRadius: 10,
    borderWidth: 1.5,
    borderColor: '#000',
    alignItems: 'center',
    justifyContent: 'center',
  },
  selectedRb: {
    width: 10,
    height: 10,
    borderRadius: 5,
    backgroundColor: '#000',
  },
  payButton: {
    marginTop: 30,
    backgroundColor: '#000',
    paddingVertical: 12,
    borderRadius: 8,
    alignItems: 'center',
  },
  payText: {
    color: 'white',
    fontSize: 16,
    fontWeight: '600',
  },
});

