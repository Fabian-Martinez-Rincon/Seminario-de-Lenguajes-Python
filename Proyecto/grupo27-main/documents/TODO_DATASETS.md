# Changes for each dataset

### Spotify

The following transformations must be done:

- Musical genders to 'title case', exept for acronyms, EDM, DFW, UK, R&B and LGBTQ+ that must be in 'upper case'

- If a gender contains a '-' must be treated as two separated words

- Only 'Top Genre', 'Year Released', 'BPM', 'Top Year', 'Artist Type' and 'Artist' columns must stay, discard any other if exist

- The new column other must be :

    | Top Genre | Artist Type | Year Released | Top Year | BPM | Artist |
    | :-: | :-: | :-: | :-: | :-: | :-: |

<br>

### Lakes

The following transformations must be done:

- Column 'Coordenadas' must be in decimal degrees unit intead of degrees, minutes and seconds

- Only 'Ubicación', 'Superficie (km²)', 'Profundidad máxima (m)', 'Profundidad media (m)', 'Coordenadas' and 'Nombre' columns must stay, discard any other if exist

- The new column other must be :

    | Ubicación | Superficie (km²) | Profundidad máxima (m) | Profundidad media (m) | Coordenadas | Nombre |
    | :-: | :-: | :-: | :-: | :-: | :-: |

<br>

### FIFA

The following transformations must be done:

- For column 'Potential', replace the numerical values with the corresponding classification in the table:

    | Value | Classification |
    | :-: | :-: |
    | < 60 | Regular |
    | >= 60, < 80 | Bueno |
    | >= 80, < 90 | Muy bueno |
    | >= 90 | Sobresaliente |

- For column 'Position', replace the acronym with the corresponding classification in the table:

    | Acronym | Classification |
    | :-: | :-: |
    | ST | Delantero |
    | CM | Volante |
    | CDM | Volante defensivo |
    | LB | Lateral Izquierdo |
    | GK | Arquero |
    | LM | Volante izquierdo |
    | RM | Volante derecho |
    | CAM | Volante offensivo |
    | LW | Volante izquierdo ofensivo |
    | LWB | Lateral izquierdo ofensivo |
    | CB | Defensor central |
    | RB | Lateral derecho |
    | RW | Volante ofensivo derecho |
    | RWB | Lateral ofensivo derecho |
    | CF | Media punta |
    

- Only 'Age', 'Nationality', 'Position', 'Team', 'Potential' and 'Name' columns must stay, discard any other if exist

- The new column other must be :

    | Team | Nationality | Position | Age | Potential | Name |
    | :-: | :-: | :-: | :-: | :-: | :-: |
