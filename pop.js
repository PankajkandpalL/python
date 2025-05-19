import React, { useState } from 'react';
import {
  SafeAreaView,
  View,
  Text,
  FlatList,
  StyleSheet,
  TouchableOpacity,
} from 'react-native';

const mockData = [
  {
    id: '1',
    orderId: '#ASKL7896',
    date: 'Tuesday, July 23 at 5:05pm',
    amount: 820,
    status: 'Refund',
    payment: { wallet: 300, gateway: 520 },
    method: 'Mixed',
  },
  {
    id: '2',
    orderId: '#ASKL7896',
    date: 'Tuesday, July 23 at 5:05pm',
    amount: 820,
    status: 'Completed',
    payment: { currency: 300 },
    method: 'PL Currency',
  },
  {
    id: '3',
    orderId: '#ASKL7896',
    date: 'Tuesday, July 23 at 5:05pm',
    amount: 820,
    status: 'Failed',
    payment: { currency: 300 },
    method: 'PL Currency',
  },
  {
    id: '4',
    orderId: '#ASKL7896',
    date: 'Tuesday, July 23 at 5:05pm',
    amount: 820,
    status: 'In Progress',
    payment: { wallet: 300 },
    method: 'PL Wallet',
  },
];

const filters = ['All', 'PL Wallet', 'PL Currency'];

const statusColors = {
  Refund: '#c9f1dd',
  Completed: '#d2f1e1',
  Failed: '#f5c7c7',
  'In Progress': '#ffe8c4',
};

export default function App() {
  const [activeFilter, setActiveFilter] = useState('All');

  const filteredData =
    activeFilter === 'All'
      ? mockData
      : mockData.filter(item => item.method === activeFilter);

  const renderItem = ({ item }) => (
    <View style={styles.card}>
      <View style={styles.row}>
        <Text style={styles.orderId}>Order ID: {item.orderId}</Text>
        <Text style={styles.amount}>₹{item.amount}</Text>
      </View>
      <Text style={styles.date}>{item.date}</Text>
      <Text style={styles.paidVia}>Paid via</Text>
      {item.payment.wallet && (
        <Text style={styles.paymentMethod}>PL Wallet: ₹{item.payment.wallet}</Text>
      )}
      {item.payment.currency && (
        <Text style={styles.paymentMethod}>PL Currency: ₹{item.payment.currency}</Text>
      )}
      {item.payment.gateway && (
        <Text style={styles.paymentMethod}>Pay U: ₹{item.payment.gateway}</Text>
      )}
      <View
        style={[
          styles.statusTag,
          { backgroundColor: statusColors[item.status] || '#eee' },
        ]}
      >
        <Text style={styles.statusText}>{item.status}</Text>
      </View>
    </View>
  );

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.filterRow}>
        {filters.map(filter => (
          <TouchableOpacity
            key={filter}
            style={[
              styles.filterButton,
              activeFilter === filter && styles.activeFilter,
            ]}
            onPress={() => setActiveFilter(filter)}
          >
            <Text
              style={[
                styles.filterText,
                activeFilter === filter && styles.activeFilterText,
              ]}
            >
              {filter}
            </Text>
          </TouchableOpacity>
        ))}
      </View>
      <FlatList
        data={filteredData}
        keyExtractor={item => item.id}
        renderItem={renderItem}
        contentContainerStyle={{ paddingBottom: 20 }}
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f6f6f6' },
  filterRow: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    paddingVertical: 12,
    backgroundColor: '#fff',
  },
  filterButton: {
    paddingHorizontal: 16,
    paddingVertical: 6,
    borderRadius: 20,
    backgroundColor: '#eee',
  },
  activeFilter: {
    backgroundColor: '#000',
  },
  filterText: {
    color: '#000',
  },
  activeFilterText: {
    color: '#fff',
  },
  card: {
    backgroundColor: '#fff',
    marginHorizontal: 16,
    marginVertical: 8,
    padding: 16,
    borderRadius: 10,
    elevation: 2,
  },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  orderId: { fontWeight: '600', fontSize: 15 },
  amount: { fontWeight: 'bold', fontSize: 16 },
  date: { color: '#666', fontSize: 13, marginVertical: 4 },
  paidVia: { marginTop: 10, fontWeight: '500' },
  paymentMethod: { fontSize: 13, color: '#444' },
  statusTag: {
    marginTop: 10,
    alignSelf: 'flex-end',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
  },
  statusText: {
    fontWeight: '600',
    color: '#333',
    fontSize: 12,
  },
});