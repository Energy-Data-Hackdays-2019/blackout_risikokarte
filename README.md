# openData_eniwa

Wir haben uns bei der Erstellung der Blackoutkarte vorerst auf das Medium Elektro beschränkt, wobei der Ansatz grundsätzlich auf andere Medien übertragen werden kann und auch für andere Grundlagedaten angewendet werden kann. Herausforderung war und wird sein passende Grundlagedaten für die Analysen zu finden. Als Tool wurde vorwiegend [QGIS](https://www.qgis.org/de/site/) verwendet

Als erstes haben wir verschiedene Gefahren definiert.
![Gefahren](https://gitlab.com/maegman/opendata_eniwa/raw/master/Dokumentation/1_Blackout%20Map.png)


Als nächstens haben wir die unterschiedlichen Karten vereinheitlicht und normert, damit sie im nächsten Schritt miteinander verrechnet werden können. So wurden die unterschiedlichen Farben in hohes Risiken mit dem Wert 200, mittleres Risiko 100 und geringes Risiko 50 konvertiert. Die normierten Risiken wurden nun zusammen addiert. Die Risiken können beim addieren noch unterschiedlich gewichtet werden. In unserem Beispiel haben wir die beiden verwendeten Risiken gleich gewichtet.
![Risiko](https://gitlab.com/maegman/opendata_eniwa/raw/master/Dokumentation/2_Blackout%20Map.png)


Die bestehenden Leitungen inkl. Einteilung der Wichtigkeit der Leitungen lag als CSV vor und wurde mittels [SpatialLite](https://www.gaia-gis.it/fossil/libspatialite/index) in QGIS hinzugefügt. Die gewichtete Risikokarte wurde mit den Leitungen multipliziert, wodurch die neuralgischen Punkte aufgrund Risikowahrscheinlichkeit und Relevanz der Anlagen/Leitugen ermittelt werden konnten.
![Risiko](https://gitlab.com/maegman/opendata_eniwa/raw/master/Dokumentation/3_Blackout%20Map.png)


Die gewichtete Risikokarte wurde weiter in QGIS als 3D-Map visualisiert und mit den Leitungen überlagert. 
Das Risiko bestimmt die Höhe des Geländes, das heisst je höher ein Punkt, umso wahrscheinlicher ein Vorfall.
![Blackout Karte](https://gitlab.com/maegman/opendata_eniwa/raw/master/Dokumentation/4_Blackout%20Map.png)

Die Berechnungen wurden in [Python](https://gitlab.com/maegman/opendata_eniwa/raw/master/Python/ColorUnify.py) umgesetzt und als [QGIS Analysen](https://gitlab.com/maegman/opendata_eniwa/raw/master/Dokumentation/Dokumentation_QGIS%20Analysen.pdf)
