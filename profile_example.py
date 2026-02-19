import asyncio
import tulipy    # Can be any TA library.
import octobot_script as obs
import octobot_services.constants as services_constants

async def example():
    config = {}
    profile_id = "ai_trading"

    # Read and cache candle data to make subsequent backtesting runs faster.
    data = await obs.get_data("BTC/USDT", "1d", start_timestamp=1505606400,
                              social_sources=[services_constants.ALTERNATIVE_ME_TOPIC_FEAR_AND_GREED],
                              profile_id=profile_id)
    run_data = {}
    # Run a backtest using the above data, strategy and configuration.
    res = await obs.run(data, config, profile_id=profile_id)
    print(res.describe())
    # Generate and open report including indicators plots
    await res.plot(show=True)
    # Stop data to release local databases.
    await data.stop()


# Call the execution of the script inside "asyncio.run" as
# OctoBot-Script runs using the python asyncio framework.
asyncio.run(example())
