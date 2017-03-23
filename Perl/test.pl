#!/bin/perl 
require 'test_config.pl';
#use strict; 
use IO::Socket;
use JSON;
use Data::Dumper;
#use IO::Socket::Timeout;
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
#my $output = $ARGV[2] || 'result.txt';


my $buf = undef;
my $sock = IO::Socket::INET->new(
        PeerAddr => $addr,
        PeerPort => $port,
        Proto    => 'tcp')
        or die "Can't connect: $!\n";

my $robot;

if ($type == 1) { 
        $robot = IO::Socket::INET->new(
        PeerAddr => $addr,
        PeerPort => $port,
        Proto    => 'tcp')
        or die "Can't connect: $!\n";
}


my $first_message = qq|{"devid":"$speecher_devid", "devicetype":"60", "reqtype":"sendid", "status":"", "content":""}|;
my $msg = $sock->send($first_message);

#print "send speecher first message ".$first_message.",result: $msg\n";


#binmode FD, ":encoding(utf-8)";

my $json = JSON->new->utf8;

my $format = qq|{"devid":"$speecher_devid", "devicetype":"60", "reqtype":"sendword", "status":"1", "content":"%s"}|;


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
        } else { 
                print "unkown command\n";
        }
}

print "end \n";
close $sock;
close(FD);