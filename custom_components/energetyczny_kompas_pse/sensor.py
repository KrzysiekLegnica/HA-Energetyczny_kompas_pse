import aiohttp
import async_timeout
from datetime import datetime, timedelta
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.device_registry import DeviceInfo
from .const import DOMAIN, STATE_MAPPING

API_URL = "https://api.raporty.pse.pl/api/pdgsz?$select=znacznik,udtczas&$filter=business_date eq '{date}'"

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the sensor."""
    update_interval = entry.data.get("update_interval", 6)
    async_add_entities([EnergetycznyKompasSensor(update_interval, entry)])


class EnergetycznyKompasSensor(Entity):
    """Representation of the Energetyczny Kompas sensor."""

    def __init__(self, update_interval, entry):
        self._state = None
        self._attributes = {}
        self._update_interval = timedelta(hours=update_interval)
        self._last_update = None
        self._entry_id = entry.entry_id

    @property
    def name(self):
        return "Energetyczny Kompas PSE"

    @property
    def unique_id(self):
        """Return a unique ID for this sensor."""
        return f"{DOMAIN}_{self._entry_id}"

    @property
    def device_info(self):
        """Return device info for the sensor."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._entry_id)},
            name="Energetyczny Kompas PSE",
            manufacturer="PSE",
            model="Energetyczny Kompas",
            entry_type="service",
        )

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    async def async_update(self):
        """Fetch the latest data."""
        now = datetime.now()
        if self._last_update and now - self._last_update < self._update_interval:
            return

        self._last_update = now
        today = now.strftime("%Y-%m-%d")
        url = API_URL.format(date=today)

        async with aiohttp.ClientSession() as session:
            try:
                with async_timeout.timeout(10):
                    response = await session.get(url)
                    if response.status == 200:
                        data = await response.json()
                        self._process_data(data)
            except Exception as e:
                self._attributes["error"] = str(e)

    def _process_data(self, data):
        now = datetime.now()
        current_hour = now.strftime("%Y-%m-%d %H:00:00")
        matched_entry = next(
            (entry for entry in data.get("value", []) if entry["udtczas"] == current_hour),
            None
        )

        if matched_entry:
            znacznik = matched_entry["znacznik"]
            self._state = STATE_MAPPING.get(znacznik, "UNKNOWN")
        else:
            self._state = "NO DATA"

        self._attributes["all_data"] = data.get("value", [])
