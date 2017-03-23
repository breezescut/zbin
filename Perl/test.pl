#!/bin/perl 
require 'test_config.pl';
#use strict; 
use IO::Socket;
use JSON;
use Data::Dumper;
use IO::Socket::Timeout;
use Net::MQTT::Simple;
use utf8;
#use utf8::all;

binmode STDOUT, ":utf-8";
binmode STDERR, ":utf-8";



#my $speecher_devid="3095e3020743";
#my $robot_devid = "34c3d23b768b";
my $speecher_devid="020000000000";
my $robot_devid = "robottesting";


#my $type = $ARGV[0] || 1;
my $type = 0;
my $addr = $ARGV[0] || '127.0.0.1';
my $port = $ARGV[1] || '7004';
my $mqtthost = $ARGV[2] || '47.93.80.117:1883';
#my $output = $ARGV[2] || 'result.txt';


my $buf = undef;
my $sock = IO::Socket::INET->new(
        PeerAddr => $addr,
        PeerPort => $port,
        Proto    => 'tcp')
        or die "Can't connect: $!\n";

my $m = Net::MQTT::Simple->new($mqtthost) || die("Can't connect mqtt $mqtthost:$!\n");



my $first_message = qq|{"devid":"$speecher_devid", "devicetype":"60", "reqtype":"sendid", "status":"", "content":""}|;
my $msg = $sock->send($first_message);

#print "send speecher first message ".$first_message.",result: $msg\n";


#binmode FD, ":encoding(utf-8)";

my $json = JSON->new->utf8;

my $format = qq|{"devid":"$speecher_devid", "devicetype":"60", "reqtype":"sendword", "status":"1", "content":"%s"}|;

my $pid = 0;
if ($pid = fork() > 0) { 
} elsif($pid == 0)  { 

        while (1) {
                my $heartbeat = qq|{"devicetype":"60","devid":"020000000000","reqtype":"heartbeat"}|;
                my $r = $sock->send(${heartbeat});

                sleep(20);
        }
        exit(0);
}

END{  
        if (defined($pid) && $pid > 0) { 
                kill(9, $pid);
        }
} 



while (1) { 
        print "Input option:";
        $one = <STDIN>;
        chomp($one);
        $one =~ s/[ \t]+//g;
        #print $one . "|\n";
        if ($one eq "quit") { 
                last;
        } elsif (defined($config{$one})) { 
                my $msg= sprintf($format, $config{$one}) ;
                print $msg."\n";
                my $r = $sock->send($msg);
        } elsif (defined($mqttconfig{$one})) { 
                print $mqttconfig{$one}."\n";
                my $r = $m->publish("c2s/device/50294D20A98F", $mqttconfig{$one});
        } else { 
                print "unkown command\n";
        }
}

print "end \n";
close $sock;
close(FD);
