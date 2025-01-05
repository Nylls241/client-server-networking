# Reliability Test (TCP vs UDP)

## 1. **Test Objective**

The goal was to demonstrate how **TCP** (a reliable, connection-oriented protocol) and **UDP** (a connectionless, best-effort protocol) behave during message transmission and reception, particularly **under unstable network conditions** or when messages are sent in bursts.

## 2. **Test Setup**

1. **Interactive Chat:**  
   - We created two applications (client/server) for **TCP** and two applications (client/server) for **UDP**.  
   - Each application allows text-based message exchange:
     - The **server** listens for incoming messages and can respond.
     - The **client** connects (in TCP) or sends datagrams (in UDP) and receives responses.

2. **Asynchronous Message Sending:**  
   - For each protocol, we **enabled multiple message transmissions** in quick succession without waiting for a response, using a **dedicated thread** for reception (listener) and a **main thread** for input/transmission.  
   - This setup allows message spamming and observation of behavior.

3. **Simulated Packet Loss** (optional but insightful):  
   - To **highlight** differences, we simulated an unstable network by introducing a packet loss percentage (e.g., 30%) using the command `sudo tc qdisc add dev lo root netem loss 30%` on Linux.  
   - This allowed us to observe how TCP reacts (automatic retransmissions) versus UDP (no automatic retransmissions).

## 3. **Observations**

1. **Under Normal Conditions (Minimal/No Loss):**  
   - **TCP** and **UDP** appear to behave similarly in local environments since the loopback interface (localhost) rarely loses packets.  
   - Messages generally arrive in order for TCP. For UDP (in local environments), disorder is less likely if the network does not disrupt transmissions.

2. **When Simulating Loss:**  
   - **TCP:**
     - Messages eventually arrive, sometimes with slight delays if a packet is lost (TCP detects the loss and retransmits).
     - Transmission may slow down (congestion control), but no messages are "lost."
   - **UDP:**
     - Some messages disappear with no retransmission.
     - Clients or servers may miss messages or receive them in a different order than sent.

3. **Log Examples:**  
   - With **TCP**, every sent message is eventually received, even during bursts.
   - With **UDP**, there may be "gaps": some messages are not received, or they arrive out of order.

## 4. **Results Interpretation**

1. **TCP:**  
   - Guarantees **reliability**: no message loss, automatic retransmission, ordered reception.
   - Suitable for applications prioritizing data integrity and completeness (e.g., file transfer, reliable messaging).

2. **UDP:**  
   - **Unreliable**: fast and lightweight, but no native retransmission mechanisms. Packets are sent "as-is"; lost packets are not recovered.
   - Ideal for use cases prioritizing **low latency** (e.g., streaming, VoIP) where occasional packet loss is preferable to delays caused by retransmissions.

## 5. **Test Conclusion**

- The **reliability test** demonstrated that **TCP** ensures message delivery and order, even under network disruptions, while **UDP** may lose messages or receive them out of order without warning.  
- In local environments (without packet loss), the differences are less pronounced, but when simulating packet loss or interruptions, TCP retransmits (causing slight delays) while UDP "drops" lost packets.
- This illustrates the **key difference** between these protocols in terms of **reliability**:
  - **TCP = guaranteed**, heavier.
  - **UDP = best-effort**, lighter but unreliable.

