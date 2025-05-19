import React, { useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  FlatList,
  Button,
} from 'react-native';

const WalletScreen = () => {
  const [wallets, setWallets] = useState([
    { id: '1', name: 'PL Wallet', balance: 1000 },
    { id: '2', name: 'PL Currency', balance: 1000 },
  ]);

  const [selectedWallet, setSelectedWallet] = useState(null);

  const addAmount = (amount) => {
    setWallets((prevWallets) =>
      prevWallets.map((wallet) =>
        wallet.id === selectedWallet.id
          ? { ...wallet, balance: wallet.balance + amount }
          : wallet
      )
    );
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Wallets & payments</Text>

      <FlatList
        data={wallets}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <TouchableOpacity
            style={styles.walletCard}
            onPress={() => setSelectedWallet(item)}
          >
            <Text style={styles.walletTitle}>{item.name}</Text>
            <Text style={styles.walletBalance}>₹{item.balance.toFixed(2)}</Text>
          </TouchableOpacity>
        )}
      />

      {selectedWallet && (
        <View style={styles.addMoneySection}>
          <Text style={styles.sectionTitle}>Add Money to {selectedWallet.name}</Text>
          <View style={styles.amountRow}>
            {[100, 500, 1000].map((amt) => (
              <TouchableOpacity
                key={amt}
                style={styles.amountButton}
                onPress={() => addAmount(amt)}
              >
                <Text style={styles.amountText}>+₹{amt}</Text>
              </TouchableOpacity>
            ))}
          </View>
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: { padding: 20, backgroundColor: '#fff', flex: 1 },
  title: { fontSize: 22, fontWeight: 'bold', marginBottom: 20 },
  walletCard: {
    backgroundColor: '#f2f2f2',
    padding: 16,
    borderRadius: 10,
    marginBottom: 10,
  },
  walletTitle: { fontSize: 16, fontWeight: '600' },
  walletBalance: { fontSize: 16, marginTop: 4 },
  addMoneySection: { marginTop: 30 },
  sectionTitle: { fontSize: 18, fontWeight: '600', marginBottom: 10 },
  amountRow: { flexDirection: 'row', justifyContent: 'space-around' },
  amountButton: {
    backgroundColor: '#004d40',
    paddingVertical: 12,
    paddingHorizontal: 20,
    borderRadius: 8,
  },
  amountText: { color: '#fff', fontSize: 16 },
});

export default WalletScreen;