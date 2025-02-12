class FingerPrint:
    FINGER_PRINT_LIST = [
        {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "language": "en-US",
            "platform": "Win32",
            "hardwareConcurrency": 8,
            "deviceMemory": 8,
            "screenResolution": [1920, 1080],
            "timezoneOffset": -120
        },
        {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            "language": "en-US",
            "platform": "MacIntel",
            "hardwareConcurrency": 4,
            "deviceMemory": 16,
            "screenResolution": [2560, 1600],
            "timezoneOffset": -420
        },
        {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "language": "en-US",
            "platform": "Win32",
            "hardwareConcurrency": 4,
            "deviceMemory": 4,
            "screenResolution": [1366, 768],
            "timezoneOffset": -300
        },
        {
            "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "language": "en-US",
            "platform": "Linux x86_64",
            "hardwareConcurrency": 8,
            "deviceMemory": 8,
            "screenResolution": [1920, 1080],
            "timezoneOffset": 0
        },
        {
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "language": "en-US",
            "platform": "iPhone",
            "hardwareConcurrency": 2,
            "deviceMemory": 4,
            "screenResolution": [1170, 2532],
            "timezoneOffset": -420
        },
        {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "language": "en-US",
            "platform": "Win32",
            "hardwareConcurrency": 4,
            "deviceMemory": 8,
            "screenResolution": [1600, 900],
            "timezoneOffset": -240
        },
        {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
            "language": "en-US",
            "platform": "MacIntel",
            "hardwareConcurrency": 4,
            "deviceMemory": 8,
            "screenResolution": [1440, 900],
            "timezoneOffset": -420
        },
        {
            "userAgent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "language": "en-US",
            "platform": "Win32",
            "hardwareConcurrency": 4,
            "deviceMemory": 4,
            "screenResolution": [1280, 1024],
            "timezoneOffset": -300
        },
        {
            "userAgent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "language": "en-US",
            "platform": "Linux x86_64",
            "hardwareConcurrency": 4,
            "deviceMemory": 8,
            "screenResolution": [1920, 1080],
            "timezoneOffset": 0
        },
        {
            "userAgent": "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "language": "en-US",
            "platform": "iPad",
            "hardwareConcurrency": 2,
            "deviceMemory": 4,
            "screenResolution": [2048, 2732],
            "timezoneOffset": -420
        },
        {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
            "language": "en-US",
            "platform": "Win32",
            "hardwareConcurrency": 8,
            "deviceMemory": 16,
            "screenResolution": [1920, 1080],
            "timezoneOffset": -240
        },
        {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15",
            "language": "en-US",
            "platform": "MacIntel",
            "hardwareConcurrency": 4,
            "deviceMemory": 8,
            "screenResolution": [1680, 1050],
            "timezoneOffset": -420
        },
        {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
            "language": "en-US",
            "platform": "Win32",
            "hardwareConcurrency": 4,
            "deviceMemory": 4,
            "screenResolution": [1366, 768],
            "timezoneOffset": -300
        },
        {
            "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
            "language": "en-US",
            "platform": "Linux x86_64",
            "hardwareConcurrency": 8,
            "deviceMemory": 8,
            "screenResolution": [1920, 1080],
            "timezoneOffset": 0
        },
        {
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
            "language": "en-US",
            "platform": "iPhone",
            "hardwareConcurrency": 2,
            "deviceMemory": 4,
            "screenResolution": [828, 1792],
            "timezoneOffset": -420
        },
        {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
            "language": "en-US",
            "platform": "Win32",
            "hardwareConcurrency": 4,
            "deviceMemory": 8,
            "screenResolution": [1600, 900],
            "timezoneOffset": -240
        },
        {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15",
            "language": "en-US",
            "platform": "MacIntel",
            "hardwareConcurrency": 4,
            "deviceMemory": 8,
            "screenResolution": [1440, 900],
            "timezoneOffset": -420
        },
        {
            "userAgent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
            "language": "en-US",
            "platform": "Win32",
            "hardwareConcurrency": 4,
            "deviceMemory": 4,
            "screenResolution": [1280, 1024],
            "timezoneOffset": -300
        },
        {
            "userAgent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
            "language": "en-US",
            "platform": "Linux x86_64",
            "hardwareConcurrency": 4,
            "deviceMemory": 8,
            "screenResolution": [1920, 1080],
            "timezoneOffset": 0
        },
        {
            "userAgent": "Mozilla/5.0 (iPad; CPU OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
            "language": "en-US",
            "platform": "iPad",
            "hardwareConcurrency": 2,
            "deviceMemory": 4,
            "screenResolution": [2048, 2732],
            "timezoneOffset": -420
        },
        {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "language": "en-US",
            "platform": "Win32",
            "hardwareConcurrency": 8,
            "deviceMemory": 16,
            "screenResolution": [1920, 1080],
            "timezoneOffset": -240
        },
        {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/10.1.2 Safari/605.1.15",
            "language": "en-US",
            "platform": "MacIntel",
            "hardwareConcurrency": 4,
            "deviceMemory": 8,
            "screenResolution": [1680, 1050],
            "timezoneOffset": -420
        },
        {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
            "language": "en-US",
            "platform": "Win32",
            "hardwareConcurrency": 4,
            "deviceMemory": 4,
            "screenResolution": [1366, 768],
            "timezoneOffset": -300
        },
        {
            "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "language": "en-US",
            "platform": "Linux x86_64",
            "hardwareConcurrency": 8,
            "deviceMemory": 8,
            "screenResolution": [1920, 1080],
            "timezoneOffset": 0
        },
        {
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
            "language": "en-US",
            "platform": "iPhone",
            "hardwareConcurrency": 2,
            "deviceMemory": 4,
            "screenResolution": [828, 1792],
            "timezoneOffset": -420
        }
    ]