#!/bin/bash
# IT-Education-Lab Management Tool

function start_lab() {
    echo "Starting IT-Education-Lab..."
    cd lab_infra && docker-compose up -d
    echo "Wait for services to be healthy..."
    sleep 10
    docker-compose ps
}

function stop_lab() {
    echo "Stopping IT-Education-Lab..."
    cd lab_infra && docker-compose down
}

function test_scenarios() {
    echo "Testing Scenarios..."
    # Test SSTI
    RES=\$(curl -s "http://localhost:5000/vuln_ssti?name={{7*7}}")
    if [[ \$RES == *"49"* ]]; then
        echo "✅ Scenario 1 (SSTI) is VULNERABLE."
    else
        echo "❌ Scenario 1 (SSTI) test FAILED."
    fi
}

case "\$1" in
    start) start_lab ;;
    stop) stop_lab ;;
    test) test_scenarios ;;
    *) echo "Usage: \$0 {start|stop|test}" ;;
esac
