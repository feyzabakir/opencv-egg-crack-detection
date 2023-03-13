import cv2

# Goruntuyu ac
image = cv2.imread("egg.jpg")
image = cv2.resize(image,(500,400), interpolation=cv2.INTER_AREA)
cv2.imshow("Orijinal", image)

# Grayscale'e cevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny kenar tespiti algoritmasini uygula
edged = cv2.Canny(gray, 40, 200)
cv2.imshow("Canny Kenar Tespiti", edged)

# Kontur bulma
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Konturlarin cizimi
# -1 parametresi kullanilarak tum hepsi cizdirilir
cv2.drawContours(image, contours, -1, (0, 0, 255), 3)

cv2.imshow("Konturlar", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
