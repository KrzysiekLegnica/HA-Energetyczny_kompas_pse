[![HACS Default][hacs_shield]][hacs]
[![GitHub Latest Release][releases_shield]][latest_release]

[hacs_shield]: https://img.shields.io/static/v1.svg?label=HACS&message=Default&style=popout&color=green&labelColor=41bdf5&logo=HomeAssistantCommunityStore&logoColor=white
[hacs]: https://hacs.xyz/docs/default_repositories

[latest_release]: https://github.com/KrzysiekLegnica/HA-Enegretyczny_kompas_pse/releases/latest
[releases_shield]: https://img.shields.io/github/release/PiotrMachowski/Home-Assistant-custom-components-Tauron-AMIplus.svg?style=popout


Energetyczny Kompas PSE https://www.energetycznykompas.pl/  to integracja Home Assistant, która dostarcza senspor zwracający zalecane zachowanie w stosunku do energii elektrcznej na podstawie danych Polskich Sieci Energetycznych. To dodatek który odzwięrciedla dane prezentowane w aplikacji Energetyczny Kompas PSE. Na podstawie tych danych Tauron będzie przeliczał ceny w ramach taryfy G14Dynamic.

## Możliwe stany
- ZALECANE UŻYTKOWANIE
- NORMALNE UŻYTKOWANIE
- ZALECANE OSZCZĘDZANIE
- WYMAGANE OGRANICZANIE

## Instalacja
1. Dodaj to repozytorium jako niestandardowe w HACS.
2. Zainstaluj integrację i zrestartuj Home Assistant.
3. Sensor pojawi się automatycznie.

## Licencja
MIT
