# ReCoil
Reverse Communication Inter Link
- small practice for secure reverse shell engineering -

Schritt 1: Reverse Shell
1. Was node.py tun soll:

    TCP-Verbindung zu listener.py herstellen

    auf Kommandos warten

    Kommando ausführen (subprocess.getoutput(cmd))

    Output zurücksenden

2. Was listener.py tun soll:

    auf TCP-Port lauschen (bind, listen, accept)

    mit einem Node kommunizieren

    Befehle eingeben (über input()), an den Node senden

    empfangenen Output anzeigen

==> Noch zu testen.

Schritt 2: AES Verschlüsselung der Kommunikation

          [Node]                              [Listener]
             │                                    │
    gen b_priv, b_pub                            │
             │────── send b_pub ────────────────▶│
             │                                    │
                                      gen a_priv, a_pub
             │◀────── send a_pub ────────────────│
             │                                    │
   shared = b_priv * a_pub           shared = a_priv * b_pub
             │                                    │
     AES key = SHA256(shared.x)       AES key = SHA256(shared.x)

