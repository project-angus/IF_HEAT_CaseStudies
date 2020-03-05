
#SOURCE_TERM
 $PCS_TYPE
  HEAT_TRANSPORT
 $PRIMARY_VARIABLE
  TEMPERATURE1
 $GEO_TYPE
  POINT P_BHE
 $CONTRAFLOW_PIPES
; indicator d_0_i d_0_o d_1_i d_1_o w lambda_0 lambda_1
  1 .0262 .032 .0262 .032 .059397 .38 .38
; fluid: lambda, mu, c, rho
 .65 5.2e-4 4130 1000
  3  ; number of segments
; N L D lambda_g
  5 10. 0.12 2.3  ; Boden
8 80. 0.12 2.3  ; Boden
5 10. 0.12 2.3  ; Boden
 $CONTRAFLOW_INPUT
  1  ; number of data sets (steps)
3600  0      $FLOW_RATE       $INFLOW_TEMPERATURE
 $DIS_TYPE
  CONSTANT_NEUMANN 1.

#STOP


